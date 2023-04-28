import { error } from "@sveltejs/kit";
import type { Item } from "../../../types/items.js";

export const load = async ({ params, fetch }) => {
    let categoryID = params.categoryID;
    if (!categoryID) throw error(404, "Category not found");

    let categoryItems: Item[] = [];

    const res = await fetch(
        `http://127.0.0.1:5000/items/category/${categoryID}`
    );
    if (res.ok) {
        const data = await res.json();
        categoryItems = data.items;
    } else {
        throw error(res.status, "Error fetching category items");
    }
    if (!categoryItems.length) throw error(404, "Category not found");

    return { categoryItems, categoryID };
};
