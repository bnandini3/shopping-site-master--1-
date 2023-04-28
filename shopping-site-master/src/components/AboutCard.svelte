<script lang="ts">
    export let member: {
        id: number;
        name: string;
        email: string;
        contributions: string;
        image: string;
    };
</script>

<div class="student-card">
    <img src={"/images/members/" + member.image} alt={member.name} />
    <h2 class="font-bold mb-3 text-2xl">{member.name}</h2>
    <p>Contribution: {member.contributions}</p>
    <p class="mt-4">{member.email}</p>
</div>

<style>
    .student-card {
        width: 300px;
        margin: 20px;
        padding: 20px;
        background-color: #f5f5f5;
        border-radius: 10px;
        text-align: center;
    }

    .student-card img {
        width: 150px;
        height: 150px;
        object-fit: cover;
        border-radius: 50%;
        margin: 0 auto 20px;
        display: block;
    }

    .student-card p {
        font-size: 16px;
        line-height: 1.5;
        margin-bottom: 0;
    }
</style>
