class accessing_variables():
    def __init__(self):
        self.test_env="oci_stage"
        self.oper_unit="US"

    def func1(self):
        print(f"From func1..Hello")


def main():
    obj=accessing_variables()
    if obj.test_env == "oci_stage":
        print(f"test_env is {obj.test_env}")
        
    print(obj.oper_unit)

if __name__ == '__main__':
    main()
