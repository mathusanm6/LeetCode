namespace std::views
{
    /* Returns a view that pairs each element in the input range with its corresponding index, starting from 0.
     *
     * Example usage:
     * ```
     * for (auto [index, value] : std::views::enumerate(container)) {
     *     // Use index and value
     * }
     * ```
     *
     * @tparam Range The type of the input range.
     * @param range The input range to enumerate.
     * @return A view of pairs, where each pair consists of an index and the corresponding element from the input range.
     */
    template <typename Range>
    auto enumerate(Range &&range)
    {
        return std::views::zip(std::views::iota(0), std::forward<Range>(range));
    }
}