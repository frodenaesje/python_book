# ex_08_07_student_register

See the textbook for the exercise text.

## Assessment criteria

| Criterion | Description | Weight (%) |
|---|---|---:|
| Student initialization and count | Initializes each Student with the supplied name, ID and GPA in the required Student instance attributes, and provides the shared creation count through get_count(). | 20 |
| Validated GPA property | Provides a readable and writable gpa property accepting values from 0.0 through 4.0 and rejecting out-of-range initialization and updates with ValueError. | 20 |
| Register storage and membership | Maintains an independent list of Student objects, adds students, removes students by ID, reports missing IDs, and returns the current register size through len(). | 20 |
| Name search | Returns a list of all Student objects whose names contain the search text, ignoring case, or an empty list when none match. | 15 |
| GPA comparison and top students | Implements __lt__() by GPA and uses Student comparison to return up to the requested number of highest-GPA students in descending order. | 15 |
| String representations | Returns readable Student strings containing name, ID and GPA, and a register string showing each stored student on a separate line. | 10 |
| **Total** | | **100%** |
