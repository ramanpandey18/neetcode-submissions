/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
            
        // Min-heap based on the node's value
        PriorityQueue<ListNode> heap = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));
        
        // Push the head of each list into the heap
        for (ListNode node : lists) {
            if (node != null) {
                heap.offer(node);
            }
        }
        
        ListNode dummy = new ListNode();
        ListNode cur = dummy;
        
        // O(N log K) where N is total nodes, K is number of lists
        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            cur.next = node;
            cur = node;
            
            node = node.next;
            if (node != null) {
                heap.offer(node);
            }
        }
        
        return dummy.next;
    }
}
        