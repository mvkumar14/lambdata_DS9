class Cleaning():
    def __init__(self, df):
        self.df = df
        pass

    def drop_null_cols(self, percent):
        """
        A funciton to drop a column if a certain percent of its values
        are null
        """
        if percent > 1:
            percent = percent/100
        a = self.df
        for col in a.columns:
            total_nans = a[col].isna().sum()
            size = a.shape[1]
            if (total_nans/size) >= percent:
                a.drop(col)
                print(f"column {col} will be dropped")
            else:
                print(f"column {col} will not be dropped")

    def to_null(self, column, value=[0]):
        """
        Replace all values in a column with np.nan. Useful when values like 0
        might actually be nan values.

        The parameter column would have to be a string.
        """
        if type(value) != list:
            value = [value]
        a = self.df
        a[column] = a[column].replace(value, np.nan)
        return a
