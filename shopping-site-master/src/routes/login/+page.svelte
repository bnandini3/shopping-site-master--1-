<script lang="ts">
    import { goto } from "$app/navigation";
    import currentUser from "../../stores/user";

    let username: string = "";
    let password: string = "";
    const login = async () => {
        const res = await fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        });
        if (res.status === 401) {
            alert("Incorrect username or password!");
            return;
        }
        if (res.status === 400) {
            alert("Please enter a username and password!");
            return;
        }
        if (res.status !== 200) {
            alert("Something went wrong!");
            return;
        }
        currentUser.set(username);
        alert("Login successful!");
        goto("/");
    };
</script>

<section class="login">
    <div class="form-container">
        <h2 class="font-bold text-2xl text-center mb-5">Login</h2>

        <form on:submit|preventDefault={login}>
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
            <button type="submit">Login</button>
        </form>
        <br />
        <p>Don't have an account? <a href="/signup">Sign up here</a>.</p>
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
