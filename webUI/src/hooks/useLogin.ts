import { ref } from 'vue'

export const useLogin = () => {
  const bgImg = ref<string>('https://cn.bing.com/th?id=OHR.ChateauLoire_EN-CN0222939171_1920x1080.webp&qlt=50')

  return {
    bgImg,
  }
}
