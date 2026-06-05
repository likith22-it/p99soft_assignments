class User {
    constructor(builder) {
        this.name = builder.name;
        this.email = builder.email;
        this.age = builder.age;
        this.address = builder.address;
        this.phone = builder.phone;
    }
}

class UserBuilder {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }

    setAge(age) {
        this.age = age;
        return this;
    }

    setAddress(address) {
        this.address = address;
        return this;
    }

    setPhone(phone) {
        this.phone = phone;
        return this;
    }

    build() {
        return new User(this);
    }
}

module.exports = UserBuilder;