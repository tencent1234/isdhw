def BinarySearch(list, select):
    is_none=False
    iflists!=[]:
    cen_num =len(lists)/2
    tlag=lists[cen_num]
    gt_list=lists[0:cen_num]
    lt_list=lists[cen_num+1:]
    
if  tlag==select:
    is_none=True
    return is_none
elif tlag>select:
     is_se=BinarySearch(gt_list,select)
     if notis_se:
        return BinarySearch(lt_list,select)
      return is_none
elif tlag<select:
    is_se=BinarySearch(lt_list,select)
     if notis_se:
        return BinarySearch(gt_list,select)
      return is_none
    
