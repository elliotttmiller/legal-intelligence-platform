"""Document comparison and redlining tools"""
import logging
from typing import List, Dict, Any
from difflib import SequenceMatcher

logger = logging.getLogger(__name__)


class DocumentComparisonEngine:
    """Advanced document comparison optimized for legal contract negotiation"""
    
    async def compare_documents(
        self,
        doc_a_text: str,
        doc_b_text: str,
        doc_a_id: str = "doc_a",
        doc_b_id: str = "doc_b"
    ) -> Dict[str, Any]:
        """
        Perform detailed comparison between two documents.
        
        Designed for contract negotiation workflows, identifying material changes
        and legal implications of differences.
        
        Args:
            doc_a_text: First document text
            doc_b_text: Second document text
            doc_a_id: Identifier for first document
            doc_b_id: Identifier for second document
            
        Returns:
            Detailed comparison with redline changes and legal analysis
        """
        logger.info(f"Comparing documents {doc_a_id} and {doc_b_id}")
        
        # Perform text comparison
        differences = self._identify_differences(doc_a_text, doc_b_text)
        similarities = self._identify_similarities(doc_a_text, doc_b_text)
        
        # Analyze legal implications
        legal_implications = await self._analyze_legal_implications(differences)
        
        # Generate redline representation
        redline = self._generate_redline(doc_a_text, doc_b_text)
        
        # Provide recommendation
        recommendation = self._generate_recommendation(differences, legal_implications)
        
        return {
            "doc_a_id": doc_a_id,
            "doc_b_id": doc_b_id,
            "differences": differences,
            "similarities": similarities,
            "legal_implications": legal_implications,
            "redline_html": redline,
            "recommendation": recommendation,
            "change_count": len(differences),
            "similarity_score": self._calculate_similarity(doc_a_text, doc_b_text)
        }
    
    def _identify_differences(self, text_a: str, text_b: str) -> List[Dict[str, Any]]:
        """Identify specific differences between documents"""
        differences = []
        
        # Simplified difference detection (would use more sophisticated NLP)
        matcher = SequenceMatcher(None, text_a, text_b)
        
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != 'equal':
                differences.append({
                    "type": tag,
                    "original_text": text_a[i1:i2] if i1 < i2 else "",
                    "modified_text": text_b[j1:j2] if j1 < j2 else "",
                    "position": i1,
                    "severity": "material"  # Would be determined by legal analysis
                })
        
        return differences
    
    def _identify_similarities(self, text_a: str, text_b: str) -> List[Dict[str, Any]]:
        """Identify preserved sections"""
        # Placeholder for similarity identification
        return [{
            "section": "Boilerplate provisions",
            "preservation_score": 0.95
        }]
    
    async def _analyze_legal_implications(self, differences: List[Dict[str, Any]]) -> List[str]:
        """Analyze legal implications of identified differences"""
        implications = []
        
        for diff in differences:
            if diff.get("severity") == "material":
                implications.append(
                    f"Material change in {diff['type']} may alter binding obligations"
                )
        
        return implications
    
    def _generate_redline(self, original: str, modified: str) -> str:
        """Generate HTML redline representation"""
        # Placeholder - would generate proper HTML with strikethrough and insertions
        return "<div class='redline'>Redline HTML would be generated here</div>"
    
    def _generate_recommendation(
        self,
        differences: List[Dict[str, Any]],
        legal_implications: List[str]
    ) -> str:
        """Generate professional recommendation based on comparison"""
        material_changes = sum(1 for d in differences if d.get("severity") == "material")
        
        if material_changes > 0:
            return (
                f"Review required: {material_changes} material changes identified. "
                "Attorney review recommended for binding obligation modifications."
            )
        else:
            return "Non-material changes only. Routine review adequate."
    
    def _calculate_similarity(self, text_a: str, text_b: str) -> float:
        """Calculate similarity score between documents"""
        return SequenceMatcher(None, text_a, text_b).ratio()
