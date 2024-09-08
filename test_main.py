"""
Test File
"""

from main_python import read_csv_file, generalise_data, line_graph_visualisation
import pandas as pd

# string IO helps create a csv file for testing
from io import StringIO
import matplotlib.pyplot as plt


def test_read_csv_file():
    csv_data = """col1,col2
                    10,20
                    30,40"""
    csv_file = StringIO(csv_data)

    result_df = read_csv_file(csv_file)

    # Check the dataframe has correct data
    assert result_df.shape == (2, 1)
    # assert list(result_df.columns) == ["col1", "col2"]


def test_describe_column():
    csv_data = """A,B,C
                        1,4,7
                        2,5,8
                        3,6,9"""
    test_df = pd.read_csv(StringIO(csv_data))
    description = generalise_data(test_df, "A")

    # Check if the description contains expected values
    assert description.loc["mean"].values[0] == 2
    assert description.loc["count"].values[0] == 3


def test_plot_line_graph():
    csv_data = """Pos,PTS
                  PG,25
                  SG,20
                  SF,22
                  PF,19
                  C,23"""
    test_df = pd.read_csv(StringIO(csv_data))

    try:
        # Test plot, but not displaying it
        plt.figure()
        line_graph_visualisation(test_df, 'Pos', 'PTS', "Average Points by Position", "Player Position", "Average Points")
        plot_success = True
    except Exception as e:
        plot_success = False
        print(f"Plot failed: {e}")

    assert plot_success

if __name__ == "__main__":
    test_read_csv_file()
    test_describe_column()
    test_plot_line_graph()
