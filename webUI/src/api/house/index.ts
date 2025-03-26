import { request } from '@/utils/service';

export const getHouseApi = () => {
  return request({
    url: '/house_data/get_house_data',
    method: 'get',
  });
};
