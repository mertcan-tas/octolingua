import { createI18n } from "vue-i18n";

const i18n = createI18n({
  locale: "tr",
  fallbackLocale: "en",
  messages: {
    tr: {
      message: {
        hello: "Merhaba!",
      },
    },
    en: {
      message: {
        hello: "Hello!",
      },
    },
  },
});

export default i18n;
