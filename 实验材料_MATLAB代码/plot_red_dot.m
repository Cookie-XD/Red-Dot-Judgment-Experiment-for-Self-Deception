%%
loop_num = 150;
prompt = 1;
left = 0;
xx = [-0.1 10.1];
yy = xx;
point_distance = 0.09;

for i = 1 : loop_num
    
    [x1, y1] = y_gt_x_rand(21, point_distance);
    [y2, x2] = y_gt_x_rand(19, point_distance);
%     left = 0;
    if left == 1
        x = [x1; x2];
        y = [y1; y2];
%         left = 1;
    else
        y = [x1; x2];
        x = [y1; y2];
%         left = 0;
    end
    f1 = figure;
    circles(x,y,0.08,'color','red', 'EdgeColor','red')
    set(gcf,'unit','normalized','position',[0.2,0.2,0.4,0.64]);
    box on
    xticks(xx)
    yticks(yy)
    xticklabels({'',''})
    yticklabels({'',''})
    hold on
    plot(xx, yy, 'Color', '#312520')
    axis([xx yy])
    disp(sum(x < y))
    if left == 1
        filename = ['_left_' int2str(i) '.png'];
    else
        filename = [ '_right_' int2str(i) '.png'];
    end
    if prompt == 1
        filename = ['With_prompt' filename];
        if left == 1
            text(-0.8,10.5,'左','FontSize',40, 'Color', 'red')
        else
            text(-0.8,10.5,'右','FontSize',40, 'Color', 'red')
        end
    else
        filename = ['No_prompt' filename];
    end
    text(10.5,-0.5,"a ",'FontSize',40, 'Color', 'white')
    set(gca,'position',[0.08 0.08 0.84 0.84])
    % saveas(f1, filename)
    f = gcf;
    % saveas(f, filename)
    exportgraphics(f,'testtt.png','Resolution',300, 'Bounds','loose')
    % export_fig tmp.png -transparent -r600
    % movefile('tmp.png', filename);
    close(f1)
end