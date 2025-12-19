"""
Professional Metrics - Workflow efficiency tracking
"""
from datetime import datetime
from typing import List, Dict
import json


class WorkflowMetricsTracker:
    """Track and analyze lawyer workflow efficiency metrics"""
    
    def __init__(self):
        self.metrics_log = []
        
    def record_task_completion(
        self,
        task_type: str,
        automated_time: float,
        estimated_manual_time: float,
        accuracy_score: float = None
    ):
        """
        Record completion of an automated task.
        
        Args:
            task_type: Type of task completed
            automated_time: Actual time taken by automation (hours)
            estimated_manual_time: Estimated manual completion time (hours)
            accuracy_score: Optional accuracy assessment (0-1)
        """
        time_saved = estimated_manual_time - automated_time
        savings_percentage = (time_saved / estimated_manual_time) * 100
        
        metric = {
            'timestamp': datetime.utcnow().isoformat(),
            'task_type': task_type,
            'automated_time': automated_time,
            'estimated_manual_time': estimated_manual_time,
            'time_saved': time_saved,
            'savings_percentage': savings_percentage,
            'accuracy_score': accuracy_score
        }
        
        self.metrics_log.append(metric)
        return metric
    
    def get_aggregate_metrics(self, task_type: str = None) -> Dict:
        """
        Get aggregated workflow metrics.
        
        Args:
            task_type: Optional filter by task type
            
        Returns:
            Aggregated metrics dictionary
        """
        filtered_metrics = self.metrics_log
        if task_type:
            filtered_metrics = [m for m in self.metrics_log if m['task_type'] == task_type]
        
        if not filtered_metrics:
            return {
                'total_tasks': 0,
                'total_time_saved': 0,
                'average_savings_percentage': 0,
                'average_accuracy': 0
            }
        
        total_time_saved = sum(m['time_saved'] for m in filtered_metrics)
        avg_savings = sum(m['savings_percentage'] for m in filtered_metrics) / len(filtered_metrics)
        
        accuracy_scores = [m['accuracy_score'] for m in filtered_metrics if m['accuracy_score'] is not None]
        avg_accuracy = sum(accuracy_scores) / len(accuracy_scores) if accuracy_scores else 0
        
        return {
            'total_tasks': len(filtered_metrics),
            'total_time_saved': round(total_time_saved, 2),
            'average_savings_percentage': round(avg_savings, 2),
            'average_accuracy': round(avg_accuracy, 2),
            'by_task_type': self._get_task_breakdown()
        }
    
    def _get_task_breakdown(self) -> Dict:
        """Get metrics broken down by task type"""
        task_types = set(m['task_type'] for m in self.metrics_log)
        breakdown = {}
        
        for task_type in task_types:
            task_metrics = [m for m in self.metrics_log if m['task_type'] == task_type]
            breakdown[task_type] = {
                'count': len(task_metrics),
                'total_time_saved': sum(m['time_saved'] for m in task_metrics)
            }
        
        return breakdown
    
    def export_metrics(self, filepath: str):
        """Export metrics to JSON file"""
        with open(filepath, 'w') as f:
            json.dump({
                'metrics': self.metrics_log,
                'aggregates': self.get_aggregate_metrics()
            }, f, indent=2)
