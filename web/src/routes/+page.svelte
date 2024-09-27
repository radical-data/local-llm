<script lang="ts">
  import { RemoteRunnable } from "@langchain/core/runnables/remote";

  let question = "";
  let answer = "";
  let isLoading = false;

  const remoteRunnable = new RemoteRunnable({
    url: "http://localhost:8000/chain",
    options: {
      timeout: 10000000,
      headers: {
        "Content-Type": "application/json",
      },
    },
  });

  async function askLangChainAPI() {
    if (!question.trim()) return;

    isLoading = true;
    answer = "";

    try {
      const result = await remoteRunnable.invoke({
        text: question,
      });

      answer = result;
    } catch (error) {
      console.error("Error:", error);
      answer = "Error: Something went wrong";
    } finally {
      isLoading = false;
    }
  }
</script>

<main>
  <h1>Talk to the Local LLM</h1>

  <input
    placeholder="Your question"
    bind:value={question}
    on:keydown={(event) => event.key === "Enter" && askLangChainAPI()}
  />

  <button on:click={askLangChainAPI} disabled={isLoading || !question.trim()}>
    {isLoading ? "Asking..." : "Ask"}
  </button>

  {#if answer}
    <p><strong>Answer:</strong> {answer}</p>
  {/if}
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background-color: #f0f0f0;
    color: #333;
  }

  input {
    padding: 10px;
    font-size: 16px;
    width: 300px;
    margin-bottom: 10px;
  }

  button {
    padding: 10px 20px;
    font-size: 16px;
  }

  p {
    margin-top: 20px;
    font-size: 18px;
  }
</style>
