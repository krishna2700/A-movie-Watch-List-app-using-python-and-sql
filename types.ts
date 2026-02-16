// TypeScript Types - A Quick Overview

// 1. Basic Types
let name: string = "Alice";
let age: number = 30;
let active: boolean = true;

// 2. Arrays & Tuples
let scores: number[] = [90, 85, 100];
let pair: [string, number] = ["Alice", 30];

// 3. Union & Literal Types
let id: string | number = "abc123";
let direction: "up" | "down" = "up";

// 4. Interfaces – define object shapes
interface User {
  name: string;
  age: number;
  email?: string; // optional property
}

// 5. Type Aliases – create reusable type names
type Point = { x: number; y: number };
type Callback = (data: string) => void;

// 6. Generics – write flexible, reusable code
function identity<T>(value: T): T {
  return value;
}

// 7. Enums – named constants
enum Status {
  Active,
  Inactive,
  Pending,
}

// 8. Utility Types – built-in type transformers
type PartialUser = Partial<User>;     // all props optional
type ReadonlyUser = Readonly<User>;   // all props readonly
type NameOnly = Pick<User, "name">;   // subset of props
