<script lang="ts">
    let paymentSuccess = false;
</script>

<div class="mt-4">
    {#if paymentSuccess}
        <section class="flex justify-center items-center">
            <div class="form-container w-full max-w-4xl">
                <h2 class="font-bold text-2xl text-center mb-5">
                    Payment Successful
                </h2>
                <p class="text-center">
                    Thank you for your purchase. Your order will be shipped
                    within 3 business days.
                </p>
            </div>
        </section>
    {:else}
        <section class="flex justify-center items-center">
            <div class="form-container w-full max-w-4xl">
                <h2 class="font-bold text-2xl text-center mb-5">
                    Payment Information
                </h2>

                <form
                    on:submit|preventDefault={() => [(paymentSuccess = true)]}
                >
                    <label for="cardHolder">Card Holder Name:</label>
                    <input
                        type="text"
                        id="cardHolder"
                        name="cardHolder"
                        required
                        minlength="3"
                    />

                    <label for="cardNumber">Card Number:</label>
                    <input
                        type="text"
                        id="cardNumber"
                        name="cardNumber"
                        required
                        minlength="16"
                        maxlength="16"
                    />

                    <div class="flex w-full">
                        <div class="flex flex-col w-1/2 mr-4">
                            <label for="expirationDate"
                                >Expiration (mm/yy):</label
                            >

                            <input
                                type="text"
                                id="expirationDate"
                                name="expirationDate"
                                required
                            />
                        </div>
                        <div class="flex flex-col w-1/2 md:ml-4">
                            <label for="cvv">CVV:</label>
                            <input
                                type="password"
                                inputmode="numeric"
                                id="cvv"
                                name="cvv"
                                required
                                maxlength="3"
                            />
                        </div>
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </section>
    {/if}
</div>

<style>
    .form-container {
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

    @media (max-width: 768px) {
        input[type="text"],
        input[type="password"],
        button {
            margin-bottom: 10px;
        }
    }
</style>
