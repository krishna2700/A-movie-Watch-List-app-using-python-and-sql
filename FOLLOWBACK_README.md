# Followback Feature

## Overview
This feature enables users to follow each other and see who follows them back (followbacks).

## Database Schema

### New Table: followers
```sql
CREATE TABLE IF NOT EXISTS followers (
    follower_username TEXT,
    following_username TEXT,
    FOREIGN KEY(follower_username) REFERENCES users(username),
    FOREIGN KEY(following_username) REFERENCES users(username),
    PRIMARY KEY (follower_username, following_username)
);
```

## API / Functions

### follow_user(follower, following)
- **Parameters**: `follower` (str), `following` (str)
- **Description**: Makes `follower` start following `following`
- **Example**: `follow_user("alice", "bob")` - Alice follows Bob

### unfollow_user(follower, following)
- **Parameters**: `follower` (str), `following` (str)
- **Description**: Makes `follower` unfollow `following`

### get_followers(username)
- **Parameters**: `username` (str)
- **Returns**: List of users following `username`

### get_following(username)
- **Parameters**: `username` (str)
- **Returns**: List of users that `username` follows

### get_followbacks(username)
- **Parameters**: `username` (str)
- **Returns**: List of users who follow `username` AND are followed back by `username`

## Usage Example

```python
import database

# Alice follows Bob
database.follow_user("alice", "bob")

# Bob follows Alice back (followback)
database.follow_user("bob", "alice")

# Get Alice's followbacks
followbacks = database.get_followbacks("alice")
# Returns: [("bob",)] - Bob follows Alice and Alice follows Bob back
```

## Menu Options

Add to app.py:
- 9) Follow a user
- 10) Unfollow a user  
- 11) View followers
- 12) View following
- 13) View followbacks
