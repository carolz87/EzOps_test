# Usar imagem oficial do Node.js
FROM node:18

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos e instalar dependências
COPY package.json package-lock.json ./
RUN npm install

# Copiar o restante do código
COPY . .

# Build do frontend
RUN npm run build

# Servir o frontend com um servidor leve
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "4000"]

# Expor a porta do frontend
EXPOSE 4000
