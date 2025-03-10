<script setup>
import { ref } from "vue";
import api from "../services/api";

const userInput = ref("");
const response = ref("");

const sendMessage = async () => {
  try {
    const res = await api.post("/chat", null, {
  params: { input_text: userInput.value },
  headers: { "Content-Type": "application/x-www-form-urlencoded" }
});


    response.value = res.data.response;
  } catch (error) {
    console.error("Erro ao enviar mensagem:", error);
  }
};
</script>

<template>
  <div>
    <h2>Chat com LLM</h2>
    <input v-model="userInput" placeholder="Digite sua mensagem" />
    <button @click="sendMessage">Enviar</button>
    <p>Resposta: {{ response }}</p>
  </div>
</template>

<style scoped>
input {
  margin-right: 10px;
}
</style>
