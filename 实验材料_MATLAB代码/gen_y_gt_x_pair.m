function [x, y] = gen_y_gt_x_pair(point_distance)
    x = rand();
    y = rand();
    while x > y || abs((x - y)) < point_distance / 2
        x = rand();
        y = rand();
    end
end