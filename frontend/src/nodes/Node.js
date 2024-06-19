import React from 'react';
import { Handle, Position } from 'reactflow';
import './Node.scss';

/**\
 * @function Node 
 * @argument id unique id of the node - number
 * @argument type type of the node - string
 * @argument targetHandles number of target handles to render - number
 * @argument sourceHandles number of source handles to render - number
 * @argument children to be rendered. - JSX - custom field and functionality
 */

function Node({ id, type, targetHandles, sourceHandles, children }) {
    const handles = [];
    for (let i = 1; i <= targetHandles; i++) {
        handles.push(
            <Handle
                type="target"
                position={Position.Left}
                id={`${id}-${type}-${i}-output`}
                style={{ top: `${100 * i / (targetHandles + 1)}%`, backgroundColor: 'white' }}
            />
        );
    }
    for (let i = 1; i <= sourceHandles; i++) {
        handles.push(
            <Handle
                type="source"
                position={Position.Right}
                id={`${id}-${type}-${i}-value`}
                style={{ top: `${100 * i / (sourceHandles + 1)}%`, backgroundColor: 'white' }}
            />
        );
    }
    return (
        <div className={`node node-${type}`}>
            <div className='header'>{type}</div>
            <hr />
            <div className='children'>{children}</div>
            {handles}
        </div>
    );
}

export default Node;
