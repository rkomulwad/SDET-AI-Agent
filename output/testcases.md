| Test Case ID | Description | Test Type |
|---|---|---|
| TC_001 | Add a new pet with valid data | Positive |
| TC_002 | Add a new pet with missing required fields (name, photoUrls) | Negative |
| TC_003 | Add a new pet with invalid data type for a field (e.g., string for integer ID) | Negative |
| TC_004 | Add a new pet with a very long name (boundary condition) | Boundary Value |
| TC_005 | Add a new pet with an empty array for photoUrls | Boundary Value |
| TC_006 | Update an existing pet with valid data | Positive |
| TC_007 | Update a non-existent pet | Negative |
| TC_008 | Update a pet with invalid data type for status | Negative |
| TC_009 | Find pets by status with valid status (e.g., "available") | Positive |
| TC_010 | Find pets by status with invalid status | Negative |
| TC_011 | Find pets by status with multiple comma-separated statuses | Positive |
| TC_012 | Find pet by ID with valid ID | Positive |
| TC_013 | Find pet by ID with invalid ID (e.g., negative number, non-integer) | Negative |
| TC_014 | Find pet by ID with a non-existent ID | Negative |
| TC_015 | Update pet with form data - valid name and status | Positive |
| TC_016 | Update pet with form data - missing name | Negative |
| TC_017 | Update pet with form data - invalid status | Negative |
| TC_018 | Delete pet with valid ID | Positive |
| TC_019 | Delete pet with invalid ID | Negative |
| TC_020 | Delete a non-existent pet | Negative |
| TC_021 | Place an order with valid data | Positive |
| TC_022 | Place an order with missing required fields | Negative |
| TC_023 | Place an order with invalid data types | Negative |
| TC_024 | Get order by ID with valid ID | Positive |
| TC_025 | Get order by ID with invalid ID | Negative |
| TC_026 | Get order by ID with non-existent ID | Negative |
| TC_027 | Delete order by ID with valid ID | Positive |
| TC_028 | Delete order by ID with invalid ID | Negative |
| TC_029 | Create user with valid data | Positive |
| TC_030 | Create user with missing required fields | Negative |
| TC_031 | Create user with invalid data types | Negative |
| TC_032 | Get user by username with valid username | Positive |
| TC_033 | Get user by username with invalid username | Negative |
| TC_034 | Get user by username with non-existent username | Negative |
| TC_035 | Update user with valid data | Positive |
| TC_036 | Update user with missing fields | Negative |
| TC_037 | Update user with invalid data types | Negative |
| TC_038 | Delete user with valid username | Positive |
| TC_039 | Delete user with invalid username | Negative |
| TC_040 | Login with valid username and password | Positive |
| TC_041 | Login with invalid username or password | Negative |
| TC_042 | Get pet inventory - positive test | Positive |