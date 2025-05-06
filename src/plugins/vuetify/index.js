import { createVuetify } from "vuetify";
import "vuetify/styles";
import { VBtn, VTextField } from 'vuetify/components'


import "@/assets/fonts/fonts.css";

const myCustomLightTheme = {
  dark: false,
  colors: {
    primary: "#5C4CFF",
    secondary: "#99A1FE",
    background: "#FFFFFF",
    transparency: "#82bc0000",
    soft: "#F7F7F7",
    softin: "#3c3c3c",
    lightgrey: "#4B4B4B",
    danger: "#ff4b4b",
  },
  variables: {
    "font-family": "Quicksand",
  },
};

const myCustomDarkTheme = {
  dark: true,
  colors: {
    primary: "#5C4CFF",
    secondary: "#99A1FE",
    background: "#121212",
    transparency: "#82bc0000",
    soft: "#1E1E1E",
    softin: "#E0E0E0",
    lightgrey: "#B0B0B0",
    danger: "#ff4b4b",
  },
  variables: {
    "font-family": "Quicksand",
  },
};

export default createVuetify({
  theme: {
    defaultTheme: "myCustomLightTheme",
    themes: {
      myCustomLightTheme,
      myCustomDarkTheme,
    },
  },
  aliases: {
    VBtnPrimary: VBtn,
    VTextFieldPrimary: VTextField,
  },
  defaults: {
    VTextFieldPrimary: {
      color: "secondary",
      variant: "outlined",
      bgColor: "#f0f0f0",
      density: "comfortable",
      elevation: "0",
      hideDetails: true,
      rounded: "lg",
      style: {        
        fontWeight: "600",
        lineHeight: "28px",
      }
    },
    VBtnPrimary: {
      ripple: false,
      size: "large",
      elevation: 0,
      class: "text-grey",
      style: {
        borderRadius: "16px",
        borderStyle: "solid",
        borderWidth: "2px",
        borderBottomWidth: "4px",
        letterSpacing: "0.8px",
        lineHeight: "20.4px",
        position: "relative",
        overflow: "hidden",
        padding: "0 20px",
        boxShadow: "none",
        transition: "transform 0.1s, border-bottom-width 0.1s",
        fontWeight: "700",
        height: "50px",
        justifyContent: "center",
        textAlign: "center",
        color: "rgb(175, 175, 175)",
      },
    },
  },
});
