import { writable } from "svelte/store";
import type { Item } from "../types/items";

const itemsStore = writable(<Item[]>[]);

export default itemsStore;
