"""
Tests for ensemble scorer
"""
import pytest
from app.ml.ensemble import EnsembleScorer


def test_ensemble_scorer():
    """Test ensemble scorer"""
    scorer = EnsembleScorer()
    result = scorer.calculate_score(
        latitude=28.6139,
        longitude=77.2090,
        property_type="residential"
    )
    
    assert 'clima_risk_score' in result
    assert 'risk_breakdown' in result
    assert 'risk_level' in result
    assert 'confidence' in result
    
    assert 0 <= result['clima_risk_score'] <= 100
    assert result['risk_level'] in ['low', 'moderate', 'high', 'extreme']
    assert 0 <= result['confidence'] <= 1


def test_ensemble_forecast():
    """Test ensemble forecast"""
    scorer = EnsembleScorer()
    result = scorer.forecast(
        latitude=28.6139,
        longitude=77.2090,
        years=[5, 10, 15]
    )
    
    assert 'forecasts' in result
    assert len(result['forecasts']) == 3
    
    for forecast in result['forecasts']:
        assert 'year' in forecast
        assert 'predicted_clima_risk_score' in forecast
        assert 0 <= forecast['predicted_clima_risk_score'] <= 100

