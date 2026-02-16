// TypeScript Types Explained

// 1. Primitive Types
const str: string = "hello";
const num: number = 42;
const bool: boolean = true;
const nothing: null = null;
const notDefined: undefined = undefined;

// 2. Arrays
const numbers: number[] = [1, 2, 3];
const strings: Array<string> = ["a", "b", "c"];

// 3. Objects
const user: { name: string; age: number } = { name: "John", age: 30 };

// 4. Tuples - fixed-length arrays with specific types
const coordinate: [number, number] = [10, 20];

// 5. Enums - named constants
enum Color { Red, Green, Blue }
const favoriteColor: Color = Color.Blue;

// 6. Any - disables type checking (avoid when possible)
let anything: any = "could be anything";

// 7. Union Types - value can be one of multiple types
let id: string | number = 123;

// 8. Type Aliases - create reusable type definitions
type Point = { x: number; y: number };
const point: Point = { x: 5, y: 10 };

// 9. Interfaces - define object shapes
interface Person {
  name: string;
  age: number;
  greet(): void;
}

// 10. Functions - specify parameter and return types
function add(a: number, b: number): number {
  return a + b;
}

// 11. Generics - create reusable components with type variables
function identity<T>(value: T): T {
  return value;
}

// 12. Optional and Default Parameters
function greet(name: string, greeting?: string): string {
  return `${greeting || "Hello"}, ${name}`;
}

// 13. Readonly - prevents property modification
const readonlyUser: Readonly<{ name: string }> = { name: "Jane" };

// 14. Literal Types - exact values as types
let direction: "north" | "south" | "east" | "west" = "north";

// 15. Void - function returns nothing
function logMessage(msg: string): void {
  console.log(msg);
}
