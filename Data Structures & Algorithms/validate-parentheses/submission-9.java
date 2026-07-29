class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');

        Stack<Character> stack = new Stack<>();

        for (char c: s.toCharArray()){
            if (!mapping.containsKey(c)){
                stack.push(c);
            } else{
                if (stack.isEmpty() || stack.peek() != mapping.get(c)){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();

        // Map<Character, Character> mapping = new HashMap<>();
        // mapping.put(')', '(');
        // mapping.put('}', '{');
        // mapping.put(']', '[');
        
        // Stack<Character> stack = new Stack<>();
        
        // for (char c : s.toCharArray()) {
        //     if (!mapping.containsKey(c)) {
        //         stack.push(c);
        //     } else {
        //         if (stack.isEmpty() || stack.peek() != mapping.get(c)) {
        //             return false;
        //         }
        //         stack.pop();
        //     }
        // }
        // return stack.isEmpty();
    }
}
