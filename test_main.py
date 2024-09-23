from main import load_dataset, save_plot
from convert_to_markdown import save_summaries_to_markdown


def test_load_dataset():
    """Testing the add function"""
    assert load_dataset("World_Happiness_Report_2024.csv").shape == (2363, 11)
    return


if __name__ == "__main__":
    test_load_dataset()

    print("Test completed successfully")
