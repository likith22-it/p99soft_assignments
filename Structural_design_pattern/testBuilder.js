const UserBuilder = require('./userBuilder');

const user = new UserBuilder("Likith", "likith@example.com")
    .setAge(22)
    .setAddress("Nagpur")
    .setPhone("9876543210")
    .build();

console.log(user);

const user2 = new UserBuilder("John Doe", "john@example.com")
    .setAge(30)
    .setAddress("New York")
    .setPhone("1234567890")
    .build();

console.log(user2);