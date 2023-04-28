<script>
    import AboutCard from "../../components/AboutCard.svelte";

    const aboutData = [
        {
            id: 1,
            name: "Ajita Kandapu",
            email: "ajitak@usf.edu",
            contributions:
                "I used JavaScript to help construct the login, add-to-cart, and D3.js features for our e-commerce website.",
            image: "ajita.jpg",
        },
        {
            id: 2,
            name: "Shivani Reddy Donthireddy",
            email: "shivanireddy@usf.edu",
            contributions:
                "I contributed to the development of the login,add-to-cart  and D3.js functionality for our ecommerce website using Javascript. Specifically, I wrote code to handle user input and manipulate the DOM to update the website's content dynamically.",
            image: "shivani.jpg",
        },
        {
            id: 3,
            name: "Nandini Bethamcharla",
            email: "nandinibethamcharla@usf.edu",
            contributions:
                "Worked on styling of the payment webpage, developing checkout button functionality, adding categories dropdown menu, and adding more relavant images to the men, women, and kids pages.",
            image: "nandini.jpg",
        },
        {
            id: 4,
            name: "Pavan",
            email: "boppana12@usf.edu",
            contributions:
                "My contribution to the project focuses on creating a responsive UI and UX design that enhanced the overall shopping experience for users. I also developed a checkout functionality and payment page using JavaScript, making the payment process more user-friendly. Additionally, I integrated API calls to enable dynamic content and improve site performance. I incorporated event handling, D3.js, and DOM manipulation to create a seamless user experience.",
            image: "pavan.jpg",
        },
    ];
</script>

<div class="student-section">
    {#each aboutData as member (member.id)}
        <AboutCard {member} />
    {/each}
</div>

<style>
    .student-section {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-bottom: 100px;
    }
</style>
