import { writable } from "svelte/store";
import type { CartItem } from "../types/items";
const cartStore = writable(new Map<string, CartItem>());

export default cartStore;
