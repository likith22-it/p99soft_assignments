class Animal {
    String name = "Animal";
}

class Dog extends Animal {
    String name = "Dog";

    void show() {
        System.out.println(super.name); // Animal
        System.out.println(name);       // Dog
    }
}

class Main {
    public static void main(String[] args) {

        Animal obj = new Animal();
        System.out.println(obj.name); // ✅ correct

        Dog d = new Dog();
        d.show(); // to see super keyword usage
    }
}