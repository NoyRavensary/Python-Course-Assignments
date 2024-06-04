import pandas as pd
from computation import compute_volume_change

def test_compute_volume_change():
    # Sample data
    data = {
        'mutant': ['vector', 'vector', 'FtsH', 'FtsH', 'K6L', 'K6L'],
        'time': [0, 90, 0, 90, 0, 90],
        'Volume': [4318020, 4632029, 2653577, 1215993, 3490740, 4100000]
    }
    df = pd.DataFrame(data)
    
    # Expected results
    expected_results = {
        'vector': (4632029 / 4318020) * 100,
        'FtsH': (1215993 / 2653577) * 100,
        'K6L': (4100000 / 3490740) * 100
    }
    
    # Compute the results
    actual_results = compute_volume_change(df)
    
    # Verify the results
    for mutant in expected_results:
        assert actual_results[mutant] == expected_results[mutant]
    print("All tests passed!")
