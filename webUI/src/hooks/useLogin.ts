import { ref, computed, reactive, onMounted } from 'vue';
import { getLoginCodeApi } from '@/api/login';

interface Login {
  username: string;
  password: string;
  code: string;
}

export const useLogin = () => {
  const bgImg = ref<string>('https://cn.bing.com/th?id=OHR.ChateauLoire_EN-CN0222939171_1920x1080.webp&qlt=50');
  const loginForm = reactive<Login>({
    username: '',
    password: '',
    code: '',
  });
  const codeUrl = ref<string>('');
  const createCode = () => {
    getLoginCodeApi().then((res) => {
      console.log(res);
      codeUrl.value = 'data:image/png;base64,' + res.data.img;
    });
  };
  const login = () => {
    console.log('login');
  };
  const bgStyle = computed(() => {
    return {
      backgroundImage: `url(${bgImg.value})`,
    };
  });

  onMounted(() => {
    createCode();
  });
  return {
    bgImg,
    bgStyle,
    loginForm,
    codeUrl,
    createCode,
    login,
  };
};
// https://cn.bing.com/th?id=OHR.PandaSnow_EN-CN0483430610_1920x1080.webp&qlt=50
// url("/th?id=OHR.PandaSnow_EN-CN0483430610_1920x1080.webp&qlt=50")
