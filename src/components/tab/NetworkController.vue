<template></template>

<script>
import { Loading } from "notiflix/build/notiflix-loading-aio";

export default {
  name: "NetworkController",

  data() {
    return {
      isOnline: navigator.onLine,
      connectionTimer: null,
    };
  },

  mounted() {
    if (!this.isOnline) {
      Loading.dots("Internet bağlantısı bekleniyor...", {
        clickToClose: false,
        fontFamily: "Lato, sans-serif",
        messageFontSize: "17px",
        svgSize: "70px",
        svgColor: "#ffffff"
      });
    }

    window.addEventListener("online", this.handleOnline);
    window.addEventListener("offline", this.handleOffline);
  },

  beforeDestroy() {
    window.removeEventListener("online", this.handleOnline);
    window.removeEventListener("offline", this.handleOffline);
    Loading.remove();

    if (this.connectionTimer) {
      clearTimeout(this.connectionTimer);
    }
  },

  methods: {
    handleOnline() {
      this.isOnline = true;
      Loading.remove();
      this.$emit("connection-restored");

      if (this.connectionTimer) {
        clearTimeout(this.connectionTimer);
        this.connectionTimer = null;
      }
    },

    handleOffline() {
      this.isOnline = false;
      if (this.connectionTimer) {
        clearTimeout(this.connectionTimer);
        this.connectionTimer = null;
      }

      Loading.custom("İnternet bağlantısı kesildi...", {
        customSvgCode:
          '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512" height="512" x="0" y="0" viewBox="0 0 24 24" style="enable-background:new 0 0 512 512" xml:space="preserve" class=""><g><path fill="#ffffff" fill-rule="evenodd" d="M11.331 11.324c.44-.099.9-.099 1.34 0 .732.164 1.267.672 1.745 1.304.47.623.978 1.495 1.607 2.578l.052.09c.583 1.002 1.055 1.815 1.34 2.481.29.676.46 1.361.227 2.045-.139.409-.374.778-.683 1.082-.506.497-1.194.678-1.953.763-.753.083-1.734.083-2.957.083h-.095c-1.223 0-2.205 0-2.958-.083-.759-.085-1.447-.266-1.953-.763a2.768 2.768 0 0 1-.683-1.082c-.233-.683-.063-1.369.227-2.045.285-.666.758-1.48 1.34-2.482l.052-.09c.63-1.082 1.137-1.954 1.607-2.576.478-.633 1.013-1.14 1.745-1.305zm.67 2.926a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0V15a.75.75 0 0 1 .75-.75zm-.75 4.25a.75.75 0 0 1 .75-.75h.01a.75.75 0 0 1 0 1.5H12a.75.75 0 0 1-.75-.75z" clip-rule="evenodd" opacity="1" data-original="#65008d" class=""></path><g fill="#b288bd"><path d="M22.646 6.236C19.34 3.443 15.696 2 12.001 2 8.306 2 4.663 3.443 1.356 6.236a1 1 0 1 0 1.29 1.528C5.655 5.224 8.854 4 12.001 4c3.147 0 6.346 1.223 9.355 3.764a1 1 0 0 0 1.29-1.528z" fill="#ffffff" opacity="1" data-original="#b288bd" class=""></path><path d="M19.164 9.251C15.007 5.573 9.22 5.599 4.86 9.231a1 1 0 0 0 1.28 1.537c3.64-3.034 8.319-3.008 11.697-.019a1 1 0 0 0 1.326-1.498z" fill="#ffffff" opacity="1" data-original="#b288bd" class=""></path></g></g></svg>',
        clickToClose: false,
        fontFamily: "Lato, sans-serif",
        messageFontSize: "17px",
        svgSize: "100px",
      });

      this.$emit("connection-lost");
    },

    checkConnection() {
      return this.isOnline;
    },
  },
};
</script>
