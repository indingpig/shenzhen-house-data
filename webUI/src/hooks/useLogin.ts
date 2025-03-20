import { ref, computed, reactive, onMounted } from 'vue';
import { getLoginCodeApi, loginApi } from '@/api/login';

interface Login {
  username: string;
  password: string;
  code: string;
  uuid: string;
}

export const useLogin = () => {
  const bgImg = ref<string>('https://cn.bing.com/th?id=OHR.ChateauLoire_EN-CN0222939171_1920x1080.webp&qlt=50');
  const loginForm = reactive<Login>({
    username: '',
    password: '',
    code: '',
    uuid: '',
  });
  const codeUrl = ref<string>('');
  const createCode = () => {
    getLoginCodeApi().then((res) => {
      loginForm.uuid = res.data.uuid;
      codeUrl.value = 'data:image/png;base64,' + res.data.img;
    });
  };
  const login = () => {
    loginApi(loginForm).then((res) => {
      console.log(res);
    });
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
