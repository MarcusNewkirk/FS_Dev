def arithmetic_arranger(problems):





    if len(problems) > 5:
        return "Error: Too many problems."

    for num in range(len(problems)):

        operation = num.split()

        if operation not in "+""-":
            return "Error: Operator must be '+' or '-'."

        if len(operation[0]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        elif len(operation[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            oprand1 = int(operation[0])
            oprand2 = int(operation[2])

        except ValueError:
            return "Error: Numbers must only contain digits."
          
        pr_problems = f"""
        {oprand1}
       {operation[1]} {oprand2}
        """
    arranged_problems = pr_problems
        
    return arranged_problems

       





