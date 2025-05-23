import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  srcDir: "src/",
  css: ["~/assets/css/tailwind.css"],

  modules: ["shadcn-nuxt", "@nuxt/image", "@pinia/nuxt"],
  shadcn: {
    prefix: "S",
    componentDir: "src/components/ui",
  },

  vite: {
    plugins: [
      tailwindcss(),
    ],
  },

  routeRules: {
    '/api/**': {
      proxy: process.env.NODE_ENV === "development" ? "http://127.0.0.1:8000/api/**" : "/api/**",
    },
    '/docs': {
      proxy: "http://127.0.0.1:8000/docs",
    },
    '/openapi.json': {
      proxy: "http://127.0.0.1:8000/openapi.json",
    }
  },

  nitro: {
    vercel: {
      config: {
        routes: [{
          "src": "/api/(.*)",
          "dest": "api/index.py"
        }]
      }
    }
  }
})