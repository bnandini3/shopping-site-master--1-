<script lang="ts">
    import ProductCard from "../../../components/ProductCard.svelte";

    export let data;
</script>

<svelte:head>
    <title
        >{data.categoryID.charAt(0).toUpperCase() + data.categoryID.slice(1)}'s
        Category Home Page</title
    >
</svelte:head>
<div class="mx-8 mt-4">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {#each data.categoryItems as item (item.id)}
            <ProductCard {item} />
        {/each}
    </div>
</div>
