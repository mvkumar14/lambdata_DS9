class Cleaning():
    def __init__(self, df):
        self.df = df
        pass

    def drop_null_cols(self, percent, also_zero):
        """
        A funciton to drop the

        Future Work:
        add another argument that is a list of values and/or conditions for
        values that will allow people to specify other value
        """
        a = self.df
        for col in a.columns:
            total_nans = a.col.isna().sum()
            size = a.length #check syntax here, might be .shape[1]
            if total_nans/size >= percent:
                a.drop(col)

    def to_null(self, column, value=[0]):
        """
        Replace all values in a column with np.nan. Useful when values like 0
        might actually be nan values.

        The parameter column would have to be a string.
        """
        if type(value) != list:
            value = list(value)
        a = self.df
        a = a.column.replace(value, np.nan)
        return a
    # Not sure if I should be returning a new dataframe, or if I should do the
    # changes inline. I could allow for an inline variable like the pandas api,
    # that would allow a user to determine what output they want.\

    def test(self):


