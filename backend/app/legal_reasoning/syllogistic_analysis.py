"""Formal legal reasoning and syllogistic analysis"""
import logging
from typing import List, Dict, Any

from app.models.schemas import (
    LegalSyllogism,
    ArgumentAnalysis,
    AuthorityReference,
    ConfidenceLevel
)

logger = logging.getLogger(__name__)


class SyllogisticAnalysisEngine:
    """Formal legal reasoning analysis engine"""
    
    async def analyze_argument(
        self,
        argument_text: str,
        include_counter_arguments: bool = True
    ) -> ArgumentAnalysis:
        """
        Analyze legal argument structure using formal syllogistic logic.
        
        Identifies premises, conclusions, logical coherence, and potential weaknesses.
        
        Args:
            argument_text: Text containing legal argument
            include_counter_arguments: Include counter-argument identification
            
        Returns:
            Complete argument analysis with strength assessment
        """
        logger.info("Starting syllogistic argument analysis")
        
        # Extract syllogisms from argument
        syllogisms = await self._extract_syllogisms(argument_text)
        
        # Identify strengths
        strengths = await self._identify_strengths(syllogisms)
        
        # Identify weaknesses
        weaknesses = await self._identify_weaknesses(syllogisms)
        
        # Generate counter-arguments if requested
        counter_arguments = []
        if include_counter_arguments:
            counter_arguments = await self._generate_counter_arguments(syllogisms)
        
        # Assess overall strength
        overall_strength = self._assess_overall_strength(syllogisms, weaknesses)
        
        # Generate improvement suggestions
        improvements = self._suggest_improvements(weaknesses)
        
        return ArgumentAnalysis(
            argument_id=f"arg_{hash(argument_text) % 10000}",
            syllogisms=syllogisms,
            strengths=strengths,
            weaknesses=weaknesses,
            counter_arguments=counter_arguments,
            overall_strength=overall_strength,
            improvement_suggestions=improvements
        )
    
    async def _extract_syllogisms(self, argument_text: str) -> List[LegalSyllogism]:
        """Extract formal syllogisms from legal argument"""
        # Placeholder implementation - would use NLP to identify logical structure
        syllogism = LegalSyllogism(
            major_premise="All contracts require consideration to be enforceable",
            minor_premise="This agreement lacks consideration",
            conclusion="Therefore, this agreement is unenforceable",
            supporting_authorities=[
                AuthorityReference(
                    citation="Restatement (Second) of Contracts § 71",
                    authority_type="restatement",
                    jurisdiction="National",
                    relevance_score=0.95,
                    summary="Defines consideration requirement",
                    hierarchy_level=1
                )
            ],
            strength_assessment=ConfidenceLevel.HIGH
        )
        
        return [syllogism]
    
    async def _identify_strengths(self, syllogisms: List[LegalSyllogism]) -> List[str]:
        """Identify strengths in legal argument"""
        strengths = []
        
        for syllogism in syllogisms:
            if syllogism.strength_assessment == ConfidenceLevel.HIGH:
                strengths.append(
                    f"Strong logical structure with authoritative support: {syllogism.conclusion}"
                )
            if syllogism.supporting_authorities:
                strengths.append(
                    f"Well-supported by {len(syllogism.supporting_authorities)} authorities"
                )
        
        return strengths
    
    async def _identify_weaknesses(self, syllogisms: List[LegalSyllogism]) -> List[str]:
        """Identify weaknesses in legal argument"""
        weaknesses = []
        
        for syllogism in syllogisms:
            if syllogism.strength_assessment == ConfidenceLevel.LOW:
                weaknesses.append("Weak logical connection between premises and conclusion")
            
            if not syllogism.supporting_authorities:
                weaknesses.append("Insufficient authoritative support for major premise")
        
        return weaknesses
    
    async def _generate_counter_arguments(
        self,
        syllogisms: List[LegalSyllogism]
    ) -> List[str]:
        """Generate potential counter-arguments"""
        counter_arguments = []
        
        for syllogism in syllogisms:
            counter_arguments.append(
                f"Counter: Alternative interpretation of {syllogism.major_premise} "
                "under modern contract doctrine"
            )
        
        return counter_arguments
    
    def _assess_overall_strength(
        self,
        syllogisms: List[LegalSyllogism],
        weaknesses: List[str]
    ) -> ConfidenceLevel:
        """Assess overall argument strength"""
        if not syllogisms:
            return ConfidenceLevel.LOW
        
        strong_count = sum(
            1 for s in syllogisms if s.strength_assessment == ConfidenceLevel.HIGH
        )
        
        if len(weaknesses) > len(syllogisms):
            return ConfidenceLevel.LOW
        elif strong_count >= len(syllogisms) * 0.7:
            return ConfidenceLevel.HIGH
        else:
            return ConfidenceLevel.MEDIUM
    
    def _suggest_improvements(self, weaknesses: List[str]) -> List[str]:
        """Suggest improvements to strengthen argument"""
        suggestions = []
        
        if any("insufficient" in w.lower() for w in weaknesses):
            suggestions.append("Add additional authoritative citations to support premises")
        
        if any("weak logical" in w.lower() for w in weaknesses):
            suggestions.append("Clarify logical connection with intermediate steps")
        
        return suggestions
