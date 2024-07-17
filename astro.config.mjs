import { defineConfig } from 'astro/config';

import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  load: [async () => ({
    base: process.env.NODE_ENV === 'production' ? '/kailand/' : '/',
    site: {
      keywords: ['kailand', 'sitio', 'web', 'minecraft', 'kailand v', 'server'],
      url: 'https://www.kailand.es'
    }
  })],
  integrations: [tailwind()]
});