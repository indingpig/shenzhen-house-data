import { ref, computed, reactive, onMounted } from 'vue';
import { getLoginCodeApi, loginApi, getBingImgApi } from '@/api/login';

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
  const dayCount = ref<number>(0);
  const createCode = () => {
    getLoginCodeApi().then((res) => {
      loginForm.uuid = res.uuid;
      codeUrl.value = 'data:image/png;base64,' + res.img;
    });
  };
  const login = () => {
    loginApi(loginForm).then((res) => {
      console.log(res);
    });
  };
  const previous = () => {
    dayCount.value++;
    if (dayCount.value > 6) {
      dayCount.value = 6;
    }
    getBingImg(dayCount.value);
  };
  const next = () => {
    dayCount.value--;
    if (dayCount.value < 0) {
      dayCount.value = 0;
    }
    getBingImg(dayCount.value);
  };

  const getBingImg = (day: number) => {
    getBingImgApi(day).then((res) => {
      bgImg.value = `https://cn.bing.com${res.url}`;
      console.log(res);
    });
  };

  const bgStyle = computed(() => {
    return {
      backgroundImage: `url(${bgImg.value})`,
    };
  });

  // https://s.cn.bing.net/th?id=OHR.SpringequinoxY25_EN-CN0950494692_UHD.jpg&w=3840&h=2160&c=8&rs=1&o=3&r=0
  // https://cn.bing.com//th?id=OHR.BlackHeron_EN-CN0706890689_1920x1080.jpg
  // https://cn.bing.com/th?id=OHR.SedonaSpring_EN-CN0578273058_UHD.jpg

  onMounted(() => {
    createCode();
    getBingImg(dayCount.value);
  });
  return {
    bgImg,
    bgStyle,
    loginForm,
    codeUrl,
    createCode,
    login,
    previous,
    next,
  };
};
// https://cn.bing.com/th?id=OHR.PandaSnow_EN-CN0483430610_1920x1080.webp&qlt=50
// url("/th?id=OHR.PandaSnow_EN-CN0483430610_1920x1080.webp&qlt=50")
