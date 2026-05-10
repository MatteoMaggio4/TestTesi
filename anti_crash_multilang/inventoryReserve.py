class InventoryReserve:
    """
    Python inventory module.
    It follows the same business rule described in sharedPolicy.ts:
    the daily limit is cumulative, not a limit on a single reservation.
    """

    def __init__(self, available_units, daily_limit=100):
        self.available_units = available_units
        self.daily_limit = daily_limit
        self.reserved_today = 0

    def reserve(self, units):
        if units <= 0:
            raise ValueError("Units must be greater than zero.")

        if units > self.available_units:
            raise ValueError("Not enough units available.")

        # BUG: checks only the current request, not the cumulative daily total.
        if units > self.daily_limit:
            raise ValueError("Daily reservation limit exceeded.")

        self.available_units -= units
        self.reserved_today += units
        return self.available_units
