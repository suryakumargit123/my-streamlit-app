
from streamlit.testing.v1 import AppTest

def test_app_interaction():
    """Test that the app loads and the button triggers success message."""
    at = AppTest.from_file("app.py").run()
    
    # 1. Check if the title is correct
    assert at.title[0].value == "📊 Data Processor App" [cite: 17]
    
    # 2. Simulate typing a name in the sidebar
    at.sidebar.text_input[0].set_value("GitHub Scout")
    at.run()
    
    # 3. Simulate clicking the button
    at.button[0].click().run()
    
    # 4. Assert that no errors occurred during interaction
    assert not at.exception [cite: 18]
