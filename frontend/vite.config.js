import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
  preview: {
    allowedHosts: ["pleasing-adaptation-production-2d6a.up.railway.app"],
  },
});
