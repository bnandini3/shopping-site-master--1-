<script lang="ts">
    import { goto } from "$app/navigation";
    import currentUser from "../../stores/user";

    let username: string = "";
    let password: string = "";
    const signup = async () => {
        const res = await fetch("http://127.0.0.1:5000/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        });
        if (res.status === 400) {
            const result: {
                message: string;
            } = await res.json();
            alert(result.message);
            return;
        }
        if (res.status !== 201) {
            alert("Something went wrong!");
            return;
        }
        currentUser.set(username);
        alert("Signup successful!");
        goto("/");
    };
</script>

<section class="login">
    <div class="form-container">
        <h2 class="font-bold text-2xl text-center mb-5">Sign Up</h2>

        <form on:submit|preventDefault={signup}>
            <label for="username">Username:</label>
            <input
                type="text"
                id="username"
                name="username"
                required
                bind:value={username}
            />
            <label for="password">Password:</label>
            <input
                type="password"
                id="password"
                name="password"
                required
                bind:value={password}
            />
            <button type="submit">Sign Up</button>
        </form>
        <br />
        <p>Already have an account? <a href="/login">Login Here</a>.</p>
    </div>
</section>

<style>
    /* Add responsive styles to the login form */
    .login {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .form-container {
        max-width: 400px;
        width: 90%;
        margin: 0 auto;
        padding: 30px;
        background-color: #f5f5f5;
        border-radius: 5px;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    }

    form {
        display: flex;
        flex-direction: column;
    }

    label {
        margin-bottom: 5px;
    }

    input[type="text"],
    input[type="password"] {
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
        border: none;
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    }

    button {
        background-color: rgb(255, 88, 0);
        color: #fff;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: rgb(255, 88, 0);
    }

    p {
        text-align: center;
    }

    a {
        color: rgb(255, 88, 0);
    }

    @media (max-width: 768px) {
        /* Make the login form stack vertically on smaller screens */
        .form-container {
            max-width: 100%;
            padding: 20px;
        }

        input[type="text"],
        input[type="password"],
        button {
            margin-bottom: 10px;
        }
    }
</style>
