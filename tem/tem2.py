
def validator_func(rules, strip=True, default=(False, None), diy_func=None, release=False):
    """函数版-返回dict,代替request.values/request.json
   :param rules:参数的校验规则,map
   :param strip:对字段进行前后过滤空格
   :param default:将"" 装换成None
   :param diy_func:自定义的对某一参数的校验函数格式: {key:func},类似check, diy_func={"a": lambda x: x + "aa"})
   :param release:发生参数校验异常后是否依然让参数进入主流程函数
   """
    args_dict = OrderedDict()
    try:
        if request.values:
            args_dict.update(request.values)
        if request.json:
            args_dict.update(request.json)
        if release:
            args_dict_copy = copy.deepcopy(args_dict)  # 下面流程异常时,是否直接使用 原参数传入f # fixme
        # strip
        if strip:
            for k in args_dict:
                if isstr(args_dict[k]):
                    args_dict[k] = args_dict[k].strip()
        # default
        if default[0]:
            for x in args_dict:
                if args_dict[x] == "":
                    args_dict[x] = default[1]
        # diy_func
        if diy_func:
            for k in args_dict:
                if k in diy_func:
                    args_dict[k] = diy_func[k](args_dict[k])
        # rules
        if rules:
            result, err = validate(rules, args_dict)
            if not result:
                return False, err
    except Exception as e:
        print("verify_args catch err: ", traceback.format_exc())  # TODO
        if release:
            return True, args_dict_copy
        else:
            return False, str(e)
    return True, args_dict


@app.route("/func", methods=["GET", "POST", "PUT"])
def func_example():
    result, request_args = validator_func(rules=rules_example, strip=True)  # 姿势 2
    if not result:
        return jsonify({"code": 500, "data": None, "err": request_args})
    a = request_args.get("a")
    b = request_args.get("b")
    c = request_args.get("c")
    d = request_args.get("d")
    e = request_args.get("e")
    f = request_args.get("f")
    g = request_args.get("g")
    h = request_args.get("h")
    i = request_args.get("i")
    j = request_args.get("j")
    k = request_args.get("k")
    l = request_args.get("l")
    m = request_args.get("m")
    status, data = todo(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m)
    if status:
        return jsonify({"code": 200, "data": data, "err": None})
    else:
        return jsonify({"code": 500, "data": None, "err": data})