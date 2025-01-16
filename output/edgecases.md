| Test Case ID | Description |
|---|---|
| TC_043 | Add a new pet with a very long description exceeding the database limits (edge case) |
| TC_044 | Add a new pet with a photoUrl that is not a valid URL (edge case) |
| TC_045 | Add a new pet with a photoUrl that points to a non-existent image (edge case) |
| TC_046 | Add a new pet with an excessively large number of tags (edge case) |
| TC_047 | Update a pet with a photoUrls array containing duplicate URLs (edge case) |
| TC_048 | Find pets by status with a very long status string (edge case) |
| TC_049 | Find pets by status with a status string containing special characters (edge case) |
| TC_050 | Find pets by tags with a very long tag string (edge case) |
| TC_051 | Find pets by tags with a tag string containing special characters (edge case) |
| TC_052 | Find pet by ID with an ID that is a very large integer (boundary value) |
| TC_053 | Find pet by ID with an ID that is a very small integer (boundary value) |
| TC_054 | Find pet by ID with an ID that is a zero (boundary value) |
| TC_055 | Update pet with form data - name with special characters (edge case) |
| TC_056 | Update pet with form data - extremely long name (boundary value) |
| TC_057 | Update pet with form data - status with special characters (edge case) |
| TC_058 | Update pet with form data - empty name (edge case) |
| TC_059 | Update pet with form data - empty status (edge case) |
| TC_060 | Delete pet with ID = 0 (boundary value)|
| TC_061 | Delete pet with a very large ID (boundary value)|
| TC_062 | Place an order with a quantity of 0 (boundary value) |
| TC_063 | Place an order with a negative quantity (edge case) |
| TC_064 | Place an order with a very large quantity exceeding inventory (edge case) |
| TC_065 | Place an order with a petId that does not exist (edge case) |
| TC_066 | Get order by ID with ID = 0 (boundary value)|
| TC_067 | Get order by ID with a very large ID (boundary value)|
| TC_068 | Delete order by ID with ID = 0 (boundary value)|
| TC_069 | Delete order by ID with a very large ID (boundary value)|
| TC_070 | Create user with a very long username exceeding database limits (edge case) |
| TC_071 | Create user with a username containing special characters (edge case) |
| TC_072 | Create user with a very long password (edge case) |
| TC_073 | Create user with a password containing only whitespace (edge case) |
| TC_074 | Get user by username with a very long username (edge case) |
| TC_075 | Get user by username with a username containing special characters (edge case) |
| TC_076 | Update user with a very long username (edge case) |
| TC_077 | Update user with a username containing special characters (edge case) |
| TC_078 | Delete user with a very long username (edge case) |
| TC_079 | Delete user with a username containing special characters (edge case) |
| TC_080 | Login with a very long username (edge case) |
| TC_081 | Login with a username containing special characters (edge case) |
| TC_082 | Login with a very long password (edge case) |
| TC_083 | Login with a password containing only whitespace (edge case) |
| TC_084 | Upload image with a very large file exceeding server limits (edge case) |
| TC_085 | Upload image with a file type not supported by the server (edge case) |
| TC_086 | Upload image with a corrupted file (edge case) |
| TC_087 | Upload image with an empty file (edge case) |