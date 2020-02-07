from flask_restful import Resource, reqparse, fields, marshal_with

article_parser = reqparse.RequestParser()
article_parser.add_argument('input_number', required=True, type=str, help='参数必填')

calculator_fields = {
    "input_number": fields.String,
    "output_number": fields.String
}


class Calculator(Resource):
    @marshal_with(fields=calculator_fields)
    def get(self):
        pass

    @marshal_with(fields=calculator_fields)
    def post(self):

        # 验证客户端输入 如不满足条件 返回400
        args = article_parser.parse_args()
        input_number = args.get("input_number")
        input_number = self.replace_num(input_number)
        flag, result = self.judge(input_number)
        if flag:
            data = {
                "output_number": result
            }
            return data, 200
        else:
            data = {
                "output_number": result
            }
            return data, 400

    @staticmethod
    def replace_num(number):
        number = number.replace("x", '*')
        number = number.replace("÷", '/')
        number = number.replace("%", '/100')
        return number

    @staticmethod
    def judge(number):
        try:
            for num in number:
                if num in ["*", "/", "+", "-", "."]:
                    pass
                else:
                    int(num)
            result = eval(number)
            flag = 1
        except Exception as e:
            flag = 0
            result = "输入有误"
        return flag, result
