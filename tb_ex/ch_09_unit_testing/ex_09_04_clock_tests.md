# ex_09_04_clock_tests

See the textbook for the exercise text.

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Clock implementation | Completes inc_day(), inc_month() and inc_year() with correct month lengths, leap-year handling and rollover between methods. | 40 |
| Day-boundary tests | Checks normal days, both 30- and 31-day month ends, February 28 in leap and non-leap years, and February 29 rollover with explicit expected dates. | 30 |
| Month and year tests | Checks normal month increments, December-to-January rollover and a simple year increment. | 15 |
| Full cascade test | Checks that one inc_sec() at 2023-12-31 23:59:59 produces all six expected date/time components for 2024-01-01 00:00:00. | 15 |
| **Total** | | **100%** |
