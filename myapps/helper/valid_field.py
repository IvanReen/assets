def valid_required(field, field_cn, value, errors, min_length=1, max_length=50):
    # 验证filed字段是否为必填项
    value = value.strip()
    if not value:
        errors[field] = f'{field_cn} 不能为空'
    elif len(value) < min_length:
        errors[field] = '%s 不能少于 %d 位' % (field_cn, min_length)
    elif len(value) > max_length:
        errors[field] = '%s 不能超过 %d 位' % (field_cn, max_length)
